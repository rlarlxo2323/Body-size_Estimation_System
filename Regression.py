import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def Model(sex, height, weight, age):
    df = pd.read_csv('data.CSV')
    x = df[['sex', 'height', 'weight', 'age']]

    y_shoulder = df[['shoulder']]
    y_chest = df[['chest']]
    y_waist = df[['waist']]
    y_arm = df[['arm']]
    y_hip = df[['hip']]
    y_leg = df[['leg']]

    mlr_shoulder = LinearRegression()
    mlr_chest = LinearRegression()
    mlr_waist = LinearRegression()
    mlr_arm = LinearRegression()
    mlr_hip = LinearRegression()
    mlr_leg = LinearRegression()

    mlr_shoulder.fit(x, y_shoulder)
    mlr_chest.fit(x, y_chest)
    mlr_waist.fit(x, y_waist)
    mlr_arm.fit(x, y_arm)
    mlr_hip.fit(x, y_hip)
    mlr_leg.fit(x, y_leg)

    my_size = [[sex, height, weight, age]]

    my_shoulder = round(float(mlr_shoulder.predict(my_size)), 2)
    my_chest = round(float(mlr_chest.predict(my_size)), 2)
    my_waist = round(float(mlr_waist.predict(my_size)), 2)
    my_arm = round(float(mlr_arm.predict(my_size)), 2)
    my_hip = round(float(mlr_hip.predict(my_size)), 2)
    my_leg = round(float(mlr_leg.predict(my_size)), 2)

    return [my_shoulder, my_chest, my_waist, my_arm, my_hip, my_leg]

# print("어깨 정확도", mlr_shoulder.score(x, y_shoulder))
# print("가슴 정확도", mlr_chest.score(x, y_chest))
# print("허리 정확도", mlr_waist.score(x, y_waist))
# print("팔 정확도", mlr_arm.score(x, y_arm))
# print("엉덩이 정확도", mlr_hip.score(x, y_hip))
# print("다리 정확도", mlr_leg.score(x, y_leg))

# fig, ax = plt.subplots(1, 4, figsize=(5, 5))
# ax[0].scatter(df[['height']], df[['shoulder']])
# ax[1].scatter(df[['height']], df[['chest']])
# ax[2].scatter(df[['height']], df[['waist']])
# ax[3].scatter(df[['height']], df[['leg']])
#
# ax[0].set_title('shoulder')
# ax[1].set_title('chest')
# ax[2].set_title('waist')
# ax[3].set_title('leg')
#
# plt.show()
