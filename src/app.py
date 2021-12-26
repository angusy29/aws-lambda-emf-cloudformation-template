from aws_embedded_metrics import metric_scope, MetricsLogger
from random import randint
import logging
import time
import typing

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@metric_scope
def emit_processing_latency_metrics(context: typing.Dict, start_time: float, metrics: MetricsLogger):
    metrics.put_dimensions({"FunctionName": context.function_name})
    metrics.put_metric("ProcessingLatency", time.time() - start_time, "Seconds")
    metrics.set_property("AccountId", context.invoked_function_arn.split(":")[4])
    metrics.set_property("RequestId", context.aws_request_id)
    

def handler(event: typing.Dict, context: typing.Dict):
    # 1. Perform processing
    start_time = time.time()
    logger.info(f"Processing event: {event}")
    time.sleep(randint(1, 5))

    # 2. Processing complete and emit metrics
    emit_processing_latency_metrics(context, start_time)