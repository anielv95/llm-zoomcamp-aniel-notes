[1:48 PM] Christian Mendoza Buenrostro
from azure.ai.ml.entities import AmlCompute
 
cpu_compute_target = "cpu-cluster"
 
try:

    ml_client.compute.get(cpu_compute_target)

except Exception:

    print("Creating a new cpu compute target...")

    compute = AmlCompute(

        name=cpu_compute_target, size="STANDARD_D2_V2", min_instances=0, max_instances=4

    )

    ml_client.compute.begin_create_or_update(compute).result()
 
from azure.ai.ml import command, Input
 
command_job = command(

    code="./src",

    command="python main.py --iris-csv ${{inputs.iris_csv}} --learning-rate ${{inputs.learning_rate}} --boosting ${{inputs.boosting}}",

    environment="AzureML-lightgbm-3.2-ubuntu18.04-py37-cpu@latest",

    inputs={

        "iris_csv": Input(

            type="uri_file",

            path="https://azuremlexamples.blob.core.windows.net/datasets/iris.csv",

        ),

        "learning_rate": 0.9,

        "boosting": "gbdt",

    },

    compute="cpu-cluster",

)
 
returned_job = ml_client.jobs.create_or_update(command_job)

returned_job.studio_url
 
from azure.ai.ml.entities import Model

from azure.ai.ml.constants import AssetTypes
 
run_model = Model(

    path="azureml://jobs/{}/outputs/artifacts/paths/model/".format(returned_job.name),

    name="run-model-example",

    description="Model created from run.",

    type=AssetTypes.MLFLOW_MODEL

)
 
ml_client.models.create_or_update(run_model)
