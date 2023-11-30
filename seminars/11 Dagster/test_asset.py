from dagster import asset, Output


@asset
def my_asset():
    result = [1, 2, 3]
    return Output(result, metadata={'string': 'gachi'})