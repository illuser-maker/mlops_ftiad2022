import os
from dagster import graph, op, get_dagster_logger

@op
def add(a: int, b: int) -> int:
    result = a + b
    get_dagster_logger().info(f'Result: {result}')
    return result

@op(config_schema={"num1": int})
def get_num_1(context) -> int:
    num1 = context.op_config["num1"]
    return num1

@op(config_schema={"num2": int})
def get_num_2(context) -> int:
    num2 = context.op_config["num2"]
    return num2

@op
def write_to_disk(add_result: int):
    with open('result.txt', 'w') as f:
        f.write(str(add_result))

@graph
def add_ones():
    a = get_num_1()
    b = get_num_2()
    result = add(a, b)
    write_to_disk(result)

default_config = {
    "ops": {
        "get_num_1": {
            "config": {
                "num1": 1,
            }
        },
        "get_num_2": {
            "config": {
                "num2": 2,
            }
        }
    }
}

add_ones.to_job('add_one_from_graph', config=default_config)
    
