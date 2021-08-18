# Databricks notebook source
display(dbutils.fs.ls("/databricks-datasets/learning-spark-v2/people/"))

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE default.people10m OPTIONS (PATH 'dbfs:/databricks-datasets/learning-spark-v2/people/people-10m.delta')
