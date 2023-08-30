import gradio as gr
import pandas as pd
from plans import provider_plans
from parsers import *


default_rate = 0.6

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
    print("Total consumption: %d KW"%(total_consumption))
    print('Cost: %.2f NIS' %(total_consumption * default_rate))
    discounts = []
    for provider in provider_plans:
        print(provider['provider'])
        for plan in provider['plans']:
            d = apply_plan_discount(df, plan)
            discounts.append({"Provider": provider['provider'], "Plan Name": plan['name'], "Discount [NIS]": d})

    savings_df = pd.DataFrame(discounts).sort_values(by='Discount [NIS]', ascending=False).reset_index(drop=True)
    return savings_df

def main():

    app = gr.Interface(fn=run_analysis, inputs="file", outputs="dataframe")
    app.queue(concurrency_count=2).launch()

if __name__ == "__main__":
    main()