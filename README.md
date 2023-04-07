# Export BigQuery table in xml format

We cannot directly export BQ table in xml format. Because BQ supports only four format to export BQ table. These are CSV, JSON, Avro and Parquet.

So if we need to export it in xml. Then first we need to export it into json or csv formats, which it supports. 

Here we export BQ table data in csv format and then convert those csv files in xml using python.

**Steps:**
1. Export BQ table in gcs bucket in csv format.
2. Convert  CSV files in xml
