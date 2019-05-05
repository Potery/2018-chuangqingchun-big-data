## Abstract

Our team participate in the 2018 ChuangQingChun Competition, the National Competition, which is sponsored by the Central Committee of the Communist Youth League,  and co-sponsored by China Telecom.  In the theme competition of Big Data , we propose an algorithm which judges whether the user travel by railway and predict its corresponding time. We get the fifth place in BIG DATA competition (Bronze medal).

### Introduction

> On November 8, 2013, President Xi sent a special congratulatory letter to the Organizing Committee of China Station of 2013 Global Entrepreneurship Week , emphasizing the important role of young students in innovation and entrepreneurship, and pointing out that the whole society should attach importance to and support youth innovation and entrepreneurship. The Third Plenary Session of the Eighteenth Central Committee of the Communist Party of China (CPC) made special arrangements for "improving the mechanism of promoting employment and entrepreneurship" and pointed out the clear direction. In order to implement General Secretary Xi Jinping's series of important speeches and the relevant directives of the Party Central Committee, and meet the needs of the development of college students'entrepreneurship, the Central Committee of the Communist Youth League, the Ministry of Education, the Ministry of Human Resources and Social Security, the Chinese Association of Science and Technology and the National Federation of Scholars decided to jointly organize and launch the National University of "Creating Youth" from 2014 on the basis of the original "Challenge Cup" competition for Chinese College Students The competition is held every two years.
>

Official website of ChuangQingChun Competition：http://www.chuangqingchun.net

2018 Competition：http://2018.chuangqingchun.net

Official website of "Smart Campus" Theme Competition：https://www.ctyun.cn/workcompetition/#/home

### The Schedule of  the Competition

The 2018 competition is divided into many categories. We participated in the theme competition of "ChuangQingChun " National College Students Entrepreneurship Competition "Intelligent Campus", sponsored by the Central Committee of the Communist Youth League and the "TianYiYun Cup" National College Students Entrepreneurship Competition sponsored by China Telecom Corporation. The competition is divided into creative category (development contest) and practical category (sales contest).

Creative competitions are divided into Big Data, Artificial Intelligence and other directions. We're in the big data direction.

The competition is divided into three stages:

1. August 1 - October 31, 2018: Registration & Training
2. October 31-December 2018: Preliminary Competition
3. April 2019: Finals

The preliminary result of the big data competition is the final result, which was released by China Telecom Tianyiyun Official account in WeChat on December 1, 2018.


## Result of competition

Rank List：[China Telecom Tianyiyun Official Accounts in Wechat](https://mp.weixin.qq.com/s?__biz=MzI2OTAzOTE4NA==&mid=2650750109&idx=1&sn=37a219c215ad9562faa96345c3718556&chksm=f2edffa2c59a76b45d438758e0a24976be4d3dc7e395434a432e05b0d16ddd661a801bdc9733&mpshare=1&scene=23&srcid=1201dJmfJW7SYgEYCcohohQ5&key=01d8b0a4948851bac8475ae603fa6948da1a5e657f699814fc275637504b99881bec98234fd131abc7b1fbd27cd2afb61f2e0f511f798fd5f8a60631e9c90592f2659a32e17b1222f1777c3b2bee9db0&ascene=1&uin=Mjc0NjAwODAwOA%3D%3D&devicetype=Windows+10&version=62060739&lang=zh_CN&pass_ticket=rSLRgdUe3VWRB%2BXCAcOJbu1%2FoaUkOO7W658Ohzfj04J6a0cNOElp6jHFgzwDftyY)

We get the fifth place in Big Data Direction. Rankings and awards are calculated separately in Big Data Competition. We win the bronze prize.

Awards category in all:  Gold  5, Silver 10, Bronze 30,  Excellence  10

## Problem introduction

This section is excerpted from the official website of the competition, but some rules are not strictly enforced.

### Topic

Route Recognition of Railway 
Passenger

### Mandatory Task rules 

The competitors are supposed to analyze/predict whether the users travel by rail during the particular period, the departure and arrival time according to the location data. Location information are the trajectory data of travelers between Nanjing and Shanghai through Zhenjiang, Changzhou, Wuxi and Suzhou.

Task 1: Analyze passenger trajectory, and identify all passengers who go from Nanjing to Shanghai by railway.

Task 2: If a passenger travel by railway, label the departure and arrival time. (If the passenger transfer into other transports after the train, mainly refer to the first vehicle and neglect the later ones.)

### Submission rules

(1) Before the deadline of submitting the results, the participants can submit the results of the analysis more than once, and the competition system automatically checks and scores the results as submitted.

(2) Each team is allowed to upload up to five times every single day, and each submission will cover the last one.

(3) After the competition with the announcement of rankings , the top 20 teams are required to submit no more than five slides of instructions (with codes attachment) within one week.

(4) The results are submitted in the format of  *.csv, coding in UTF-8.

(5) If the passengers travel non-railway, the corresponding departure and arrival time should be set to Zero.

### Submissions format

UID, Yes/Not by railway , Departure Time , Arrival time

Sample：

Railway Travel:         UID|1|20180111080355|20180111093718

Not Railway Travel:  UID|0|0|0

### Data

The dataset includes the following contents:

(1) Trajectory coordinates, city codes, corresponding time and unique identification of telecom users in Nanjing, Shanghai and the region between the two cities. Example:

UID | 20180111110946 | 117.2425 | 31.8325 | 83401

City code: 83101 Shanghai, 83201 Nanjing, 83202 Wuxi, 83204 Changzhou, 83205 Suzhou, 83211 Zhenjiang

(2) Railway GIS data: railway vector map data between Shanghai and Nanjing.

(3)Coordinate data of the railway station range: Boundary coordinate data of railway stations in Zhenjiang, Changzhou, Wuxi and Suzhou in Shanghai, Nanjing and the route.

(4) Highway GIS data: Vector map data of expressway between Shanghai and Nanjing.

### Scoring

Ranking score: submit validation-set answers, and rank according to the total score;

Final Score: submit test-set answers and rank them according to the total score.

1.F1score
$$
F_1=\frac{2\times P \times R}{P + R}
$$
P and R scored Precision and Recall respectively:
$$
Precision = \frac{TP}{TP+FP}
$$

$$
Recall = \frac{TP}{TP+TN}
$$

TP is the number of participants who submit answers, FP is the number of participants who actually travel by rail, FP is the number of participants who travel by rail and TN is the number of participants who actually travel by rail.

2.Scoring formula：
$$
s=\frac{1}{N}\sum_{i=0}^N((|T_1-T_1^*|)^2) \times 0.4 + (|T_2-T_2^*)^2\times 0.4 + (T_d-T_d^*)^2 \times 0.2
$$

$$
Score = 10^{-s} \times R
$$

Among them, N is the number of actual railway trips in the answers submitted by the participants. T1* and T2* are given departure arrival times, T1 and T2 are generated departure arrival times for competitors, Td is T2-T1, Td* is T1*-T2*. (Time units are hours)

The total score of the team is: the score of the first question + the score of the second question.

### Schedule

September 14: Topic release;

September 20 (23:59): Publish competition data, publish data sets (40% of all data), and use them to design algorithmic models.

October 31 (23:59): Publish test data (the remaining 60% of the data) to test the algorithm model;

Nov. 10 (23:59): At the end of the game, ranking is calculated.

November 15: Competition rankings are announced.

## Competition resources

### Cloud Server

We received a server with four core CPU and 8G Ram provided by Tianyiyun.

### Data set

Two category

1. User trace
2. Assistant data
   1. Contour of Station (Nanjing to Shanghai): Nanjing, Nanjing South, Zhenjiang, Zhenjiang South, Changzhou, North Changzhou, Wuxi, East Wuxi, Suzhou, North Suzhou, Shanghai, Hongqiao
   2. Highway Path
   3. Railway path

User trajectories are divided into two files. User_4.txt was provided at the beginning of the game, with 1.14 million rows of data, and another 1.18 million rows in November. All user trajectory data are labeled.

# Code explanation

## Overview

Random sampling, combined with visualization program, manual marking of part of the data (about more than 200 data detailed analysis)

Sample labels are divided into 2 categories (target users, non-target users) and 10 sub-categories (road trips, direction errors, roundtrip between Nanjing and Shanghai, halfway off, normal train trips, path deviations, road trips coinciding with some railways, roads approaching stations, railways without stations, other matters needing attention)

## Data Cleaning

### Overview

The data format is as described above. Each row is a uid+time+coordinate, representing the user's position at this time. There are 2.96 million rows of data, while there are 400,000 unique uid(User ID). So each user has only 7.4 coordinates in average. In fact, the data distribution is not uniform. There are a large number of users with less than 10 coordinates. The route from Nanjing to Shanghai is about 300 KM, and the number of coordinates is too small to judge. 

### Strategy

1. Omit the user with few coordinates.
2. Omit the user travels within the same city.
3. Aggregate coordinates by users and sort them by time.

## Assistant data

A large number of coordinates are given in the auxiliary data. In fact, we do not need such high precision in our strategy, so we simplify the points in the auxiliary data.

The strategy of processing line data is to calculate the slope of the line from the starting point to the following point. If the slope changes slightly, the next point is skipped. When the slope changes more than the threshold, the point is selected into the trajectory as the current point.

The method of processing station data is to select the maximum accuracy and latitude of all points as the four vertices of the station and connect them into rectangles.

## Sampling

Randomly sampling , visualize the result to help assess.

![](http://wx2.sinaimg.cn/large/007cqMIHly1g2igiux0kwj30wu0ggtid.jpg)

## Visualization Module

js+html，Baidu Map API，django

Green:  Railway

Red : Highway

Blue:  User trajectory

The Yellow circle : Railway station.

The Red label : Coordinate of user location .

Red-Edged white-background box : Time.

## Strategy Iteration

Script (Shell + Makefile)

Archive each result with time stamp, and compare this with previous data. Show the difference in two results and sampling the changed cases, in order to validate the effect of corresponding strategy.

The Pipeline of our final strategy :

### Main process（Station, Direction）

![](http://wx4.sinaimg.cn/large/007cqMIHly1g2in7nym6cj30dl0983yu.jpg)

### Secondary process (Time, Route)

![](http://wx2.sinaimg.cn/large/007cqMIHly1g2in7ftec8j30gs052aa8.jpg)

# Code Demonstration

## Main process

**l  make_datalist.py**

Used to generate pre-process data, integrate the original data points according to users, sort them in chronological order, and preliminarily filter out the non-target user based on rough location information.

**l  direction.py**

Assess if it is target user according to its macro trend of route .

**l  direction2.py**

**l  station.py**

Analysis of the relationship between user trajectory and station location.

**l  route.py**

Estimate user travel duration based on trajectory.

**l  checkline.py**

Predict user travel time based on route.

**l  aans.py**

**l  genans.py**

Integrate and generate final result.

## Other codes

**l  Makefile**

Used to integrate processes, display the dependency of respective code and data , automatically generate the result , avoid redundant calculation

**l  run.sh**

Entry towards Process One

**l  diff.sh**

Generate the difference between this result and the last one. (I.E. Increase and decrease of positive samples)

**l  get_sample.py**

Automatic Random Sampling 

**l  simplify_road.py**

Simplify Road Trajectory Information

The screenshot below shows the difference in the precision of the trajectory with three simplification algorithms,  labelled in Red, Green and Blue respectively. We use the simplified path algorithm to improve the efficiency and accuracy of the algorithm.

![](http://wx2.sinaimg.cn/large/007cqMIHly1g2in7ivq1mj30ro0aijvq.jpg)

![](http://wx4.sinaimg.cn/large/007cqMIHly1g2in7mp9d7j30q30f7jv2.jpg)

# Features

## Use makefile to avoid redundant computation

Many intermediate results occur in our algorithm, even some calculations are time consuming. When we modify the partial code, some intermediate results need not be recalculated. 'makefile'  automatically decides which code needs to be re-executed.

## Parallel computing

Design a multi-process computing method specially suitable for this project which makes full use of computing resources.

## Automated iteration

The results and intermediate codes are saved automatically. Each iteration automatically gives the difference between the present results and the last iteration, and automatically sampled.

## Utilization of External Conditions (In Future Work)

1. With the timetable of train, the "predicted time" is transformed into "predicted train number"+ "predicted advanced/Delay time"

   Take advantage of train travel characteristics:

   1. Passenger trajectories of the same train are approximately identical and synchronized

   2. Uniform speed

   3. Arrival time of intermediate node# 创青春大赛-大数据组-Team QDDX

## 项目摘要

我们参加了2018年创青春大赛，国赛，由共青团中央主办，中国电信协办的“创青春”全国大学生创业大赛“智慧校园”主题赛的创意类（开发大赛）的大数据方向的比赛，我们提出并实现了一个通过用户轨迹判断用户是否通过铁路出行，及预测出行时间的算法，获得了大数据组第五名（铜奖）。

## 背景

### 简介

> 2013年11月8日，习近平总书记向2013年全球创业周中国站活动组委会专门致贺信，特别强调了青年学生在创新创业中的重要作用，并指出全社会都应当重视和支持青年创新创业。党的十八届三中全会对"健全促进就业创业体制机制"作出了专门部署，指出了明确方向。为贯彻落实习近平总书记系列重要讲话和党中央有关指示精神，适应大学生创业发展的形势需要，在原有"挑战杯"中国大学生创业计划竞赛的基础上，共青团中央、教育部、人力资源社会保障部、中国科协、全国学联决定，自2014年起共同组织开展"创青春"全国大学生创业大赛，每两年举办一次。
>
> [^创青春官网介绍]: http://2018.chuangqingchun.net/d108/cqc/about/

创青春全国官网：http://www.chuangqingchun.net

2018国赛官网：http://2018.chuangqingchun.net

创青春全国大学生创业大赛智慧校园主题赛官网：https://www.ctyun.cn/workcompetition/#/home

### 2018年大赛

2018年大赛分为多个类别的比赛，我们参加的是共青团中央主办，中国电信集团公司承办的“天翼云杯”全国大学生云创业大赛&“创青春”全国大学生创业大赛“智慧校园”主题赛。这个比赛又分为：创意类（开发大赛）和实践类（销售大赛）。

而创意类大赛又分为大数据、人工智能等多个方向。我们参加的是大数据方向的比赛。

大赛分三阶段：

1. 2018年8月1日-10月31日：报名培训
2. 2018年10月31日-12月：初赛
3. 2019年4月：决赛

但是我们参加的大数据类比赛没有决赛，初赛结束后，于2018年12月1日由中国电信天翼云微信公众号发布了比赛结果。


## 比赛结果

结果公示：[中国电信天翼云微信公众号](https://mp.weixin.qq.com/s?__biz=MzI2OTAzOTE4NA==&mid=2650750109&idx=1&sn=37a219c215ad9562faa96345c3718556&chksm=f2edffa2c59a76b45d438758e0a24976be4d3dc7e395434a432e05b0d16ddd661a801bdc9733&mpshare=1&scene=23&srcid=1201dJmfJW7SYgEYCcohohQ5&key=01d8b0a4948851bac8475ae603fa6948da1a5e657f699814fc275637504b99881bec98234fd131abc7b1fbd27cd2afb61f2e0f511f798fd5f8a60631e9c90592f2659a32e17b1222f1777c3b2bee9db0&ascene=1&uin=Mjc0NjAwODAwOA%3D%3D&devicetype=Windows+10&version=62060739&lang=zh_CN&pass_ticket=rSLRgdUe3VWRB%2BXCAcOJbu1%2FoaUkOO7W658Ohzfj04J6a0cNOElp6jHFgzwDftyY)

我们位列大数据方向第5名（总创意类（开发大赛）第45名，但是大数据类比赛时单独计算排名和评奖的），铜奖。

比赛奖项设置：创意类：金奖5支，银奖10支，铜奖30支，优秀奖10支。

## 赛题介绍

本节内容摘自大赛官网，但是有些规则并未严格执行

### 赛题题目

铁路出行人群识别

### 赛题介绍

参赛选手需要根据所给的电信用户位置数据，预测用户在指定期间是否通过铁路出行以及出发和到达时间。位置数据为南京与上海两地间出行旅客的轨迹数据，途径镇江、常州、无锡、苏州。

任务一：分析旅客轨迹数据，识别出所有离开南京去往上海方向通过铁路出行的旅客；

任务二：若是通过铁路出行，标明出发和到达时间。（若用户乘坐火车之后换乘其他交通工具，则以第一段交通工具为准，忽视之后的换乘）

### 作品提交说明

(1)在竞赛提交结果截止时间之前，参赛者可以多次提交分析结果，竞赛系统自动为分析结果打分。

(2)每支队伍每日最多上传5次，每上传一次将覆盖上一次提交结果，以最后的提交结果为准。

(3)比赛结束，排名公布后，排名前20的队伍需在一周内提交不超过5页的参赛方法说明（附代码）。

(4)分析结果提交文件为：submission.csv，要求utf-8编码。

(5)若用户为非铁路出行，则出发到达时间均为0。

### 数据格式

用户ID,是否乘坐铁路,出发时间，到达时间

样例：

是铁路出行UID|1|20180111080355|20180111093718

非铁路出行UID|0|0|0

### 数据说明

竞赛数据集合包括以下内容：

(1)南京、上海以及两城市之间区域范围内的电信用户轨迹坐标、城市代码以及坐标对应时间和用户的唯一标识。示例：

UID|20180111110946|117.2425|31.8325|83401

城市代码：83101上海市，83201南京市，83202无锡市，83204常州市，83205苏州市，83211镇江市

(2)铁路GIS数据：上海与南京之间的铁路矢量地图数据。

(3)途径火车站范围坐标数据：上海、南京以及途径的镇江、常州、无锡、苏州各火车站的边界坐标数据。

(4)公路GIS数据：上海与南京之间的高速公路矢量地图数据。

### 评分标准

排名得分：提交验证集答案，根据总分排名；

最终得分：提交测试集答案，根据总分排名。

1.F1score
$$
F_1=\frac{2\times P \times R}{P + R}
$$
其中P和R分别为 Precision 和 Recall得分：

$$
Precision = \frac{TP}{TP+FP}
$$

$$
Recall = \frac{TP}{TP+TN}
$$

其中TP为参赛者提交答案中，通过铁路出行中实际铁路出行的人数，FP为参赛者提交答案中通过铁路出行中非铁路出行的人数，TN为参赛者提交答案中非铁路出行中实际通过铁路出行的人数。

2.评分公式：

$$
s=\frac{1}{N}\sum_{i=0}^N((|T_1-T_1^*|)^2) \times 0.4 + (|T_2-T_2^*)^2\times 0.4 + (T_d-T_d^*)^2 \times 0.2
$$

$$
Score = 10^{-s} \times R
$$

其中N为参赛者提交答案中实际铁路出行的人数。T1*和T2*为给定的出发到达时间，T1和T2为参赛者生成的出发到达时间,Td为T2-T1,Td*为T1*-T2*。（时间计算单位为小时）

参赛队伍总得分为：两题的分总为：第一题得分+第二题得分。

### 时间安排

9月14日：赛题发布；

9月20日（23:59）：公布比赛数据，发布数据集（全部数据的40%），用于设计算法模型；

10月31日（23:59）：发布测试数据（余下60%的数据），用于测试算法模型；

11月10日（23:59）：比赛结束，计算排名；

11月15日：比赛排名公布。

## 比赛资源

### 云计算

我们领取到天翼云提供的4核心8G的服务器一台。

### 数据集

分为两类

1. 用户轨迹
2. 辅助数据
   1. 车站轮廓（南京到上海）：南京、南京南、镇江、镇江南、常州、常州北、无锡、无锡东、苏州、苏州北、上海、上海虹桥
   2. 高速公路路径
   3. 铁路路径

用户轨迹分为两个文件，比赛开始时只提供了user_4.txt,114万行数据，11月又提供了另一份数据又181万行。所有用户轨迹数据均无标签。

# 代码说明

# 整体思路

随机抽样，结合可视化程序，人工标记一部分数据（大概做了200多份数据的详细分析）

样本标签分为2大类（目标用户，非目标用户）10小类（公路出行，方向错误，在南京上海间往返，中途下车，正常火车出行，路径存在偏差，公路出行与部分铁路重合，公路接近车站，铁路未经车站，其他需注意的情况）

## 数据清洗

### 数据宏观信息

数据格式如前面介绍，每行是一个uid+时间+坐标，代表这一时刻该用户的位置，总共有296万行数据，而uid有40万个，那么平均每个用户仅有7.4个坐标，实际上数据分布不均匀，存在大量用户仅有不到10个坐标，而南京到上海路线有300公里左右，坐标数量太少无法判断用户轨迹。

### 清洗策略

1. 坐标点数太少的用户舍去
2. 仅在一个城市范围内出现的用户舍去
3. 把坐标按用户聚合，并按时间排序

## 辅助数据处理

辅助数据中给出了大量坐标，实际上在我们的策略中用不到这么高的精度，所以对辅助数据中的点进行精简。

处理线路数据策略是从起点开始，计算当前点到后面点的连线的斜率，如果斜率变化小则略过下一个点，当斜率变化大于阈值，把那个点选入轨迹并作为当前点。

处理车站数据的方法是所有点中选择精度和纬度的最值作为车站的四个顶点，连成矩形。

## 抽样

采取随机抽样的策略，利用百度地图API开发可视化工具辅助判断。

![](http://wx2.sinaimg.cn/mw690/007cqMIHly1g2igiux0kwj30wu0ggtid.jpg)

## 可视化程序

js+html，利用百度地图API实现，后端使用django

绿色路径代表铁路

红色代表公路

黄色圈出的区域是火车站

红色的标签是数据中的坐标点

蓝色线条是用户的轨迹

红边白底方框中显示此点时间

## 策略迭代

设计代码自动完成全流程（shell + makefile）

每次计算结果自动添加时间标记并存档，然后和历史数据自动对比，给出新结果与之前一次结果的变化，并把变动数据自动抽样，便于迅速评估算法改进情况。

最终的方案是

### 主要流程（车站、方向）

![](http://wx1.sinaimg.cn/mw690/007cqMIHly1g2igr02pndj30d6098gm6.jpg)

### 次要流程（时间、路径）

![](http://wx3.sinaimg.cn/mw690/007cqMIHly1g2igr1s7glj30ga052dg2.jpg)

# 代码清单

## 主流程

l  make_datalist.py

用于产生预处理数据，对原始数据的点按用户整合起来，按时间顺序排序，并且可以根据粗略位置信息初步筛除非目标用户

l  direction.py

按照用户宏观走向评估用户是否是目标用户

l  direction2.py

l  station.py

分析用户轨迹与车站位置关系

l  route.py

根据轨迹估计用户出行时间

l  checkline.py

根据线路预测用户出行时间

l  aans.py

l  genans.py

用于整合生成最后的提交数据

## 辅助代码

l  Makefile

用于整合流程，指出代码、数据依赖关系，自动生成结果数据，避免不必要的重复计算

l  run.sh

流程1的入口代码

l  diff.sh

用于自动生成本次结果与上次结果的差异（正样本的增加和减少）

l  get_sample.py

自动随机抽样程序

l  simplify_road.py

化简道路轨迹信息

下面的图片用红绿蓝展示了三种不同的化简算法对轨迹描绘的精细程度的差别。

![](http://wx2.sinaimg.cn/mw690/007cqMIHly1g2in7ivq1mj30ro0aijvq.jpg)

![](http://wx4.sinaimg.cn/mw690/007cqMIHly1g2in7mp9d7j30q30f7jv2.jpg)

我们使用化简路径算法提高算法的执行效率和准确率。



# 特色

## 使用makefile避免重复计算

由于我们的算法中有很多中间结果，有些计算一次需要较长时间，当我们只修改一部分代码时，有一些中间结果不需要重算，makefile帮我们自动决定哪些代码需要重新执行。

## 并行计算

设计专门适用于本次题目的多进程计算方法，充分利用计算资源。

## 自动化迭代

自动保存每次的结果和中间代码，git实现代码版本控制，每次迭代自动给出与上次生成的结果差别，自动抽样。

## 利用外部条件（未实现）

利用火车时刻表，转化“预测时间”为“预测车次”+“预测提前/晚点时间”

利用火车出行特点：

1. 同一车次上旅客轨迹相似，时间同步

2. 速度比较均匀

3. 到达中间节点时间