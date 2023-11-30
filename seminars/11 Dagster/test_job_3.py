from dagster import graph, op, get_dagster_logger, DynamicOut, DynamicOutput, ScheduleDefinition


@op(config_schema={"nums_list": list},
    out=DynamicOut())
def get_nums(context):
    nums_list = context.op_config['nums_list']
    for num in nums_list:
        yield DynamicOutput(num, mapping_key=str(num))

@op
def square(num: int) -> int:
    return num**2

@op
def log_result(square_result):
    get_dagster_logger().info(square_result)

@graph
def square_nums():
    nums = get_nums()
    squared_nums = nums.map(square)
    log_result(squared_nums.collect())


default_config = {
    "ops": {
        "get_nums": {
            "config": {
                "nums_list": [
                    1,
                    5,
                    9
                ]
            }
        }
    }
}

square_nums_job = square_nums.to_job('square_nums', config=default_config)
schedule = ScheduleDefinition(job=square_nums_job, cron_schedule="0 * * * *")