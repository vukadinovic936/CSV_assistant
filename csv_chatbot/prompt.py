# flake8: noqa

PREFIX = """
You are working with a pandas dataframe in Python. The name of the dataframe is `df`.
You should use the tools below to answer the question posed of you:"""

MULTI_DF_PREFIX = """
You are working with {num_dfs} pandas dataframes in Python named df1, df2, etc. You 
should use the tools below to answer the question posed of you:"""

SUFFIX_NO_DF = """
Begin!
Question: {input}
{agent_scratchpad}"""

SUFFIX_WITH_DF = """
This is the result of `print(df.head())`:
{df_head}

Previous conversation history:
{history}

Begin!
Question: {input}
{agent_scratchpad}"""

SUFFIX_WITH_MULTI_DF = """
This is the result of `print(df.head())` for each dataframe:
{dfs_head}

Previous conversation history:
{history}

Begin!
Question: {input}
{agent_scratchpad}"""