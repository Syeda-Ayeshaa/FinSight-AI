def detect_anomalies(table_df):

    anomaly_flags = []

    for _, row in table_df.iterrows():

        anomaly = 0

        # Rule 1: negative values
        if row["qty"] < 0 or row["price"] < 0:
            anomaly = -1

        # Rule 2: extremely high price
        if row["price"] > 10000:
            anomaly = -1

        # Rule 3: unrealistic quantity
        if row["qty"] > 100:
            anomaly = -1

        # Rule 4: incorrect line total
        if row["line_total"] != row["qty"] * row["price"]:
            anomaly = -1

        anomaly_flags.append(anomaly)

    table_df["anomaly_flag"] = anomaly_flags

    return table_df