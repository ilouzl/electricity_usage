import pandas as pd
provider_plans = [
    {"provider": "Pazgaz", "plans":
        [
        {'name': 'unlimited', 'discount': 0.05, 'periods':  
                                                        [
                                                        {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
        },
        {'name': 'weekend', 'discount': 0.1, 'periods':
                                                    [
                                                    {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Friday", "Saturday"]
                                                    ]
        },
        {'name': 'day', 'discount': 0.15, 'periods':  
                                                    [
                                                    {"day": day, "start":pd.Timestamp('08:00:00'), "end": pd.Timestamp('15:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                    ]
        },
        {'name': 'night', 'discount': 0.15, 'periods':
                                                    [
                                                    {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('06:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                    ] 
                                                    + 
                                                    [
                                                    {"day": day, "start":pd.Timestamp('23:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                    ]
        }
        ]
    },
    {"provider": "Cellcom", "plans":
        [
        {'name': 'Work From Home', 'discount': 0.15, 'periods':  
                                                        [
                                                        {"day": day, "start":pd.Timestamp('08:00:00'), "end": pd.Timestamp('16:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
                                                        ]
        },
        {'name': 'Night Saver', 'discount': 0.2, 'periods':
                                                    [
                                                    {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('06:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
                                                    ] 
                                                    + 
                                                    [
                                                    {"day": day, "start":pd.Timestamp('22:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
                                                    ]
        }
        ]
    },
    {"provider": "AmisraGas", "plans":
        [
        {'name': 'Default', 'discount': 0.065, 'periods':  
                                                        [
                                                        {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
        }
        ]
    },
    {"provider": "Electra", "plans":
        [
        {'name': 'Power 1st year', 'discount': 0.05, 'periods':  
                                                        [
                                                        {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
        },
        {'name': 'Power 2nd year', 'discount': 0.06, 'periods':  
                                                        [
                                                        {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
        },
        {'name': 'Power 3rd year', 'discount': 0.07, 'periods':  
                                                        [
                                                        {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
        },
        {'name': 'HighTech 1st year', 'discount': 0.08, 'periods':  
                                                        [
                                                        {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('16:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
                                                        + 
                                                        [
                                                        {"day": day, "start":pd.Timestamp('23:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
        },
        {'name': 'HighTech 2nd year', 'discount': 0.09, 'periods':  
                                                        [
                                                        {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('16:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
                                                        + 
                                                        [
                                                        {"day": day, "start":pd.Timestamp('23:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
        },
        {'name': 'HighTech 3rd year', 'discount': 0.10, 'periods':  
                                                        [
                                                        {"day": day, "start":pd.Timestamp('00:00:00'), "end": pd.Timestamp('16:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
                                                        + 
                                                        [
                                                        {"day": day, "start":pd.Timestamp('23:00:00'), "end": pd.Timestamp('23:59:59')} for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                                        ]
        },

        ]
    },
]