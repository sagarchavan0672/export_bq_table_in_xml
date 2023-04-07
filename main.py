from google.cloud import bigquery
from google.cloud import storage
import pandas as pd

BQ = bigquery.Client()
CS = storage.Client()

def gcp_export_http():

    sql = """
    EXPORT DATA OPTIONS(uri="gs://bkt-dmgcp-del-ce-temp/Sagar/test/EMP_table*.csv",format='CSV', header=true, overwrite=true,
	field_delimiter=',') AS SELECT * FROM 
    dmgcp-del-ce.Test.EMP1
    """

    query_job = BQ.query(sql)  
    res = query_job.result() 
    return res

def CSVtoXML(inputfile,outputfile):
    if not inputfile.lower().endswith('.csv'):
        print('Expected A CSV File')
        return 0
    if not outputfile.lower().endswith('.xml'):
        print('Expected a XML file')
        return 0
    try:
        df=pd.read_csv(inputfile)
    except FileNotFoundError:
        print('CSV file not found')
        return 0
    entireop='<collection emp_table="EMP Details">\n'
    att=df.columns
    rowop=''
    for j in range(len(df)):
        for i in range(len(att)):
            if i==0:
                rowop=rowop+f'<{att[i]} title="{df[att[i]][j]}">\n'
            elif i==len(att)-1:
                rowop=rowop+f'<{att[i]}>{df[att[i]][j]}</{att[i]}>\n</{att[0]}>\n'
            else:
                rowop=rowop+f'<{att[i]}>{df[att[i]][j]}</{att[i]}>\n'
    entireop=entireop+rowop+'</collection>'
    with open(outputfile,'w') as f:
        f.write(entireop)


if __name__=="__main__":
    gcp_export_http()
    CSVtoXML('gs://bkt-dmgcp-del-ce-temp/Sagar/test/EMP_table000000000000.csv','EMP_table.xml')
