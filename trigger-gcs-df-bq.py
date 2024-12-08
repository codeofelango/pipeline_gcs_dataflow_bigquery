
from googleapiclient.discovery import build

def trigger_df_job(cloud_event, environment):
    """
    Triggers a Dataflow job to load data from GCS to BigQuery.

    Args:
      cloud_event: The CloudEvent object.
      environment: The environment in which the function is running.
    """
    service = build('dataflow', 'v1b3')
    project = "data-pipeline-443507"
    template_path = "gs://dataflow-templates-us-east1/latest/GCS_Text_to_BigQuery"
    template_body = {
        "jobName": "gcs_to_bigquery_textfile",  # Provide a unique name for the job
         "parameters": {
        "inputFilePattern": "gs://datapillar_datapipeline_text/employee.csv",
        "JSONPath": "gs://datapillar_datapipeline_dataflow/bq.json",
        "outputTable": "data-pipeline-443507:ingestion_text_gcs.employee",
        "bigQueryLoadingTemporaryDirectory": "gs://datapillar_datapipeline_dataflow/temp_dir",
        "javascriptTextTransformGcsPath": "gs://datapillar_datapipeline_dataflow/udf.js",
        "javascriptTextTransformFunctionName": "transform"
    }
    }
    # request = service.projects().templates().launch(projectId=project, gcsPath=template_path, body=template_body)
    # response = request.execute()
    # print(response)
    try:
        request = service.projects().templates().launch(
            projectId=project, gcsPath=template_path, body=template_body
        )
        response = request.execute()
        print(f"Dataflow job launched successfully: {response}")

    except HttpError as e:
        print(f"Error launching Dataflow job: {e}")


    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Handle other potential exceptions (e.g., network issues)
   
