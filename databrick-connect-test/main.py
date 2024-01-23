from databricks.connect import DatabricksSession
from dotenv import load_dotenv
import os 

load_dotenv()

spark = DatabricksSession.builder.remote(
  host = os.getenv("DATABRICKS_HOST_NAME"),
  token = os.getenv("DATABRICKS_ACCESS_TOKEN"),
  cluster_id = os.getenv("DATABRICKS_CLUSTER_ID")
).getOrCreate()


spark.range(1,10).show()