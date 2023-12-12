#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa



# This module records the constants used in the application

# You should define here as many constants as you need to keep your 
# code clean and legible
HOUR_CHILDBIRTH = '00h20'
MIN_CHILDBIRTH = 20
BREAK_TIME = '1h00'

# Value for weekly pause in the output schedule
WKL_PAUSE = 'weekly leave'
WKL_WORK = 2400 #minutes


# In a file:
# Number of header's lines
NUM_HEADER_LINES = 7

# Number of hour line
NUM_TIME_LINE = 3

# Next Time
TIME_30_MIN = '00h30'


# In a schedule list:
SCHED_TIME = 0
SCHED_NAME_MOTH = 1

# In a doctor's list:
# Index of the element with the docotor's name
DOCT_NAME_IDX = 0
# Index of the element with the docotor's category
DOCT_CATEGORY_IDX = 1
# Index of the element with the docotor's last childbirth
DOCT_CHILDBIRTH_IDX = 2
# Index of the element with the docotor's time daily work
DOCT_DAILYWORK_IDX = 3
# Index of the element with the docotor's time weekly work
DOCT_WEEKLYWORK_IDX = 4

# In a mother's list:
# Index of the element with the mother's name
MOTH_NAME_IDX = 0
MOTH_BRACELET_IDX = 2
MOTH_RISK_IDX = 3

