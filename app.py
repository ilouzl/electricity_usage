import gradio as gr
import pandas as pd
import plotly.express as px

from parsers import *
from plans import provider_plans

default_rate = 0.6

def power_price_txt_change(val):
    global default_rate
    default_rate = float(val)
    print(default_rate)

def apply_plan_discount(df, plan):
    total_consumption = df.consumption.sum()
    discunted_consumption = 0
    for period in plan['periods']:
        discunted_consumption += df[df.day_name == period['day']].between_time(period['start'].time(), period['end'].time()).consumption.sum()
    
    discount = discunted_consumption * plan['discount'] * default_rate
    print(f"Plan: {plan['name']}")
    # print("Discunted consumption: %d KW" %(discunted_consumption))
    print("Saving: %.2f NIS" % (discount))
    print("")
    return discount


def run_analysis(inp):
    df = read_pazgaz_report(inp.name)
    df['day_name'] = df.index.day_name()

    total_consumption = df.consumption.sum()
    discounts = []
    for provider in provider_plans:
        print(provider['provider'])
        for plan in provider['plans']:
            d = apply_plan_discount(df, plan)
            discounts.append({"Provider": provider['provider'], "Plan Name": plan['name'], "Discount [NIS]": d})

    savings_df = pd.DataFrame(discounts).sort_values(by='Discount [NIS]', ascending=False).reset_index(drop=True)

    df['ts'] = df.index
    fig = px.line(df, x="ts", y='consumption')
    df.drop(columns=['day_name'], inplace=True)
    print(df.head())
    return savings_df, fig, "Total consumption: %d KW, Cost: %.2f NIS"%(total_consumption, total_consumption * default_rate)



with gr.Blocks(title="Utility Saving Analyzer", css="style.css") as app:
    gr.Markdown("## Data Source")
    with gr.Row():
        upload_report_btn = gr.UploadButton("Upload Consumption Report", file_types=['xls', 'xlsx'], file_count='single')
        power_price_txt = gr.Textbox(label="Power Price NIS/kW", value=str(default_rate))

    total_consumption_txt = gr.Textbox(label="Total")
    consumption_plot = gr.Plot(label="Consumption Plot")
    image_stats = gr.DataFrame(label="Discounts")
    
    upload_report_btn.upload(run_analysis, inputs=upload_report_btn, outputs=[image_stats, consumption_plot, total_consumption_txt])
    power_price_txt.change(power_price_txt_change, inputs=power_price_txt)
    

app.queue(concurrency_count=2).launch()