import pandas as pd
df = pd.read_csv (r'satisfaktion.csv')

# block 1 - simple stats

# Comment évaluez-vous les méthodes pédagogique et d\'animation proposées cette semaine?
mean1 = df['Comment évaluez-vous les méthodes pédagogique et d\'animation proposées cette semaine?'].mean().round(1)
sum1 = df['Comment évaluez-vous les méthodes pédagogique et d\'animation proposées cette semaine?'].sum().round(1)
max1 = df['Comment évaluez-vous les méthodes pédagogique et d\'animation proposées cette semaine?'].max().round(1)
min1 = df['Comment évaluez-vous les méthodes pédagogique et d\'animation proposées cette semaine?'].min().round(1)
count1 = df['Comment évaluez-vous les méthodes pédagogique et d\'animation proposées cette semaine?'].count().round(1)
median1 = df['Comment évaluez-vous les méthodes pédagogique et d\'animation proposées cette semaine?'].median().round(1)
std1 = df['Comment évaluez-vous les méthodes pédagogique et d\'animation proposées cette semaine?'].std().round(1)
var1 = df['Comment évaluez-vous les méthodes pédagogique et d\'animation proposées cette semaine?'].var().round(1)


# Comment évaluez vous votre progression durant cette semaine?
mean2 = df['Comment évaluez vous votre progression durant cette semaine?'].mean().round(1)
sum2 = df['Comment évaluez vous votre progression durant cette semaine?'].sum().round(1)
max2 = df['Comment évaluez vous votre progression durant cette semaine?'].max().round(1)
min2 = df['Comment évaluez vous votre progression durant cette semaine?'].min().round(1)
count2 = df['Comment évaluez vous votre progression durant cette semaine?'].count().round(1)
median2 = df['Comment évaluez vous votre progression durant cette semaine?'].median().round(1)
std2 = df['Comment évaluez vous votre progression durant cette semaine?'].std().round(1)
var2 = df['Comment évaluez vous votre progression durant cette semaine?'].var().round(1)

# Comment évaluez vous l'évaluation matérielle de la formation?
mean3 = df['Comment évaluez vous l\'évaluation matérielle de la formation? '].mean().round(1)
sum3 = df['Comment évaluez vous l\'évaluation matérielle de la formation? '].sum().round(1)
max3 = df['Comment évaluez vous l\'évaluation matérielle de la formation? '].max().round(1)
min3 = df['Comment évaluez vous l\'évaluation matérielle de la formation? '].min().round(1)
count3 = df['Comment évaluez vous l\'évaluation matérielle de la formation? '].count().round(1)
median3 = df['Comment évaluez vous l\'évaluation matérielle de la formation? '].median().round(1)
std3 = df['Comment évaluez vous l\'évaluation matérielle de la formation? '].std().round(1)
var3 = df['Comment évaluez vous l\'évaluation matérielle de la formation? '].var().round(1)

# Votre évaluation du/des supports de cours
mean4 = df['Votre évaluation du/des supports de cours'].mean().round(1).round(1)
sum4 = df['Votre évaluation du/des supports de cours'].sum().round(1).round(1)
max4 = df['Votre évaluation du/des supports de cours'].max().round(1).round(1)
min4 = df['Votre évaluation du/des supports de cours'].min().round(1).round(1)
count4 = df['Votre évaluation du/des supports de cours'].count().round(1).round(1)
median4 = df['Votre évaluation du/des supports de cours'].median().round(1).round(1)
std4 = df['Votre évaluation du/des supports de cours'].std().round(1).round(1)
var4 = df['Votre évaluation du/des supports de cours'].var().round(1).round(1)

# Comment évaluez vous les échanges dans votre groupe?
mean5 = df['Comment évaluez vous les échanges dans votre groupe?'].mean().round(1).round(1)
sum5 = df['Comment évaluez vous les échanges dans votre groupe?'].sum().round(1).round(1)
max5 = df['Comment évaluez vous les échanges dans votre groupe?'].max().round(1).round(1)
min5 = df['Comment évaluez vous les échanges dans votre groupe?'].min().round(1).round(1)
count5 = df['Comment évaluez vous les échanges dans votre groupe?'].count().round(1).round(1)
median5 = df['Comment évaluez vous les échanges dans votre groupe?'].median().round(1).round(1)
std5 = df['Comment évaluez vous les échanges dans votre groupe?'].std().round(1).round(1)
var5 = df['Comment évaluez vous les échanges dans votre groupe?'].var().round(1).round(1)

# Comment  évaluez-vous la satisfaction de vos attentes personnelles?
mean6 = df['Comment  évaluez-vous la satisfaction de vos attentes personnelles?'].mean().round(1)
sum6 = df['Comment  évaluez-vous la satisfaction de vos attentes personnelles?'].sum().round(1)
max6 = df['Comment  évaluez-vous la satisfaction de vos attentes personnelles?'].max().round(1)
min6 = df['Comment  évaluez-vous la satisfaction de vos attentes personnelles?'].min().round(1)
count6 = df['Comment  évaluez-vous la satisfaction de vos attentes personnelles?'].count().round(1)
median6 = df['Comment  évaluez-vous la satisfaction de vos attentes personnelles?'].median().round(1)
std6 = df['Comment  évaluez-vous la satisfaction de vos attentes personnelles?'].std().round(1)
var6 = df['Comment  évaluez-vous la satisfaction de vos attentes personnelles?'].var().round(1)

# Votre évaluation sur la qualité de la documentation
mean7 = df['Votre évaluation sur la qualité de la documentation'].mean().round(1)
sum7 = df['Votre évaluation sur la qualité de la documentation'].sum().round(1)
max7 = df['Votre évaluation sur la qualité de la documentation'].max().round(1)
min7 = df['Votre évaluation sur la qualité de la documentation'].min().round(1)
count7 = df['Votre évaluation sur la qualité de la documentation'].count().round(1)
median7 = df['Votre évaluation sur la qualité de la documentation'].median().round(1)
std7 = df['Votre évaluation sur la qualité de la documentation'].std().round(1)
var7 = df['Votre évaluation sur la qualité de la documentation'].var().round(1)

# Votre avis sur le planning de la formation
mean8 = df['Votre avis sur le planning de la formation'].mean().round(1)
sum8 = df['Votre avis sur le planning de la formation'].sum().round(1)
max8 = df['Votre avis sur le planning de la formation'].max().round(1)
min8 = df['Votre avis sur le planning de la formation'].min().round(1)
count8 = df['Votre avis sur le planning de la formation'].count().round(1)
median8 = df['Votre avis sur le planning de la formation'].median().round(1)
std8 = df['Votre avis sur le planning de la formation'].std().round(1)
var8 = df['Votre avis sur le planning de la formation'].var().round(1)

# Votre avis sur les horaires
mean9 = df['Votre avis sur les horaires'].mean().round(1)
sum9 = df['Votre avis sur les horaires'].sum().round(1)
max9 = df['Votre avis sur les horaires'].max().round(1)
min9 = df['Votre avis sur les horaires'].min().round(1)
count9 = df['Votre avis sur les horaires'].count().round(1)
median9 = df['Votre avis sur les horaires'].median().round(1)
std9 = df['Votre avis sur les horaires'].std().round(1)
var9 = df['Votre avis sur les horaires'].var().round(1)

# Votre avis sur le rythme de la formation
mean10 = df['Votre avis sur le rythme de la formation'].mean().round(1)
sum10 = df['Votre avis sur le rythme de la formation'].sum().round(1)
max10 = df['Votre avis sur le rythme de la formation'].max().round(1)
min10 = df['Votre avis sur le rythme de la formation'].min().round(1)
count10 = df['Votre avis sur le rythme de la formation'].count().round(1)
median10 = df['Votre avis sur le rythme de la formation'].median().round(1)
std10 = df['Votre avis sur le rythme de la formation'].std().round(1)
var10 = df['Votre avis sur le rythme de la formation'].var().round(1)

# block 2
# group by Formation
groupby_sum1 = df.groupby(['Formation']).sum().round(1)
groupby_count1 = df.groupby(['Formation']).count().round(1)

# group by Noms
groupby_sum2 = df.groupby(['Nom']).sum().round(1)
groupby_count2 = df.groupby(['Nom']).count().round(1)

# list creation
allMeans = []
allSums = []
allMaxs = []
allMins = []
allCount = []
allMedian = []
allStd = []
allVar = []


# add data to lists
allMeans.extend([mean1, mean2, mean3, mean4, mean5, mean6, mean7, mean8, mean9, mean10])
allSums.extend([sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum9, sum10])
allMaxs.extend([max1, max2, max3, max4, max5, max6, max7, max8, max9, max10])
allMins.extend([min1, min2, min3, min4, min5, min6, min7, min8, min9, min10])
allCount.extend([count1, count2, count3, count4, count5, count6, count7, count8, count9, count10])
allMedian.extend([median1, median2, median3, median4, median5, median6, median7, median8, median9, median10])
allStd.extend([std1, std2, std3, std4, std5, std6, std7, std8, std9, std10])
allVar.extend([var1, var2, var3, var4, var5, var6, var7, var8, var9, var10])

# print block 1
print ('Mean salary: ' + str(mean1))
print ('Sum of salaries: ' + str(sum1))
print ('Max salary: ' + str(max1))
print ('Min salary: ' + str(min1))
print ('Count of salaries: ' + str(count1))
print ('Median salary: ' + str(median1))
print ('Std of salaries: ' + str(std1))
print ('Var of salaries: ' + str(var1))

# print block 2
print ('Mean salary: ' + str(mean2))
print ('Sum of salaries: ' + str(sum2))
print ('Max salary: ' + str(max2))
print ('Min salary: ' + str(min2))
print ('Count of salaries: ' + str(count2))
print ('Median salary: ' + str(median2))
print ('Std of salaries: ' + str(std2))
print ('Var of salaries: ' + str(var2))

# print block 3
print ('Mean salary: ' + str(mean3))
print ('Sum of salaries: ' + str(sum3))
print ('Max salary: ' + str(max3))
print ('Min salary: ' + str(min3))
print ('Count of salaries: ' + str(count3))
print ('Median salary: ' + str(median3))
print ('Std of salaries: ' + str(std3))
print ('Var of salaries: ' + str(var3))

# print block 4
print ('Mean salary: ' + str(mean4))
print ('Sum of salaries: ' + str(sum4))
print ('Max salary: ' + str(max4))
print ('Min salary: ' + str(min4))
print ('Count of salaries: ' + str(count4))
print ('Median salary: ' + str(median4))
print ('Std of salaries: ' + str(std4))
print ('Var of salaries: ' + str(var4))

# print block 5
print ('Mean salary: ' + str(mean5))
print ('Sum of salaries: ' + str(sum5))
print ('Max salary: ' + str(max5))
print ('Min salary: ' + str(min5))
print ('Count of salaries: ' + str(count5))
print ('Median salary: ' + str(median5))
print ('Std of salaries: ' + str(std5))
print ('Var of salaries: ' + str(var5))

# print block 6
print ('Mean salary: ' + str(mean6))
print ('Sum of salaries: ' + str(sum6))
print ('Max salary: ' + str(max6))
print ('Min salary: ' + str(min6))
print ('Count of salaries: ' + str(count6))
print ('Median salary: ' + str(median6))
print ('Std of salaries: ' + str(std6))
print ('Var of salaries: ' + str(var6))

# print block 7
print ('Mean salary: ' + str(mean7))
print ('Sum of salaries: ' + str(sum7))
print ('Max salary: ' + str(max7))
print ('Min salary: ' + str(min7))
print ('Count of salaries: ' + str(count7))
print ('Median salary: ' + str(median7))
print ('Std of salaries: ' + str(std7))
print ('Var of salaries: ' + str(var7))

# print block 8
print ('Mean salary: ' + str(mean8))
print ('Sum of salaries: ' + str(sum8))
print ('Max salary: ' + str(max8))
print ('Min salary: ' + str(min8))
print ('Count of salaries: ' + str(count8))
print ('Median salary: ' + str(median8))
print ('Std of salaries: ' + str(std8))
print ('Var of salaries: ' + str(var8))

# print block 9
print ('Mean salary: ' + str(mean9))
print ('Sum of salaries: ' + str(sum9))
print ('Max salary: ' + str(max9))
print ('Min salary: ' + str(min9))
print ('Count of salaries: ' + str(count9))
print ('Median salary: ' + str(median9))
print ('Std of salaries: ' + str(std9))
print ('Var of salaries: ' + str(var9))

# print block 10
print ('Mean salary: ' + str(mean10))
print ('Sum of salaries: ' + str(sum10))
print ('Max salary: ' + str(max10))
print ('Min salary: ' + str(min10))
print ('Count of salaries: ' + str(count10))
print ('Median salary: ' + str(median10))
print ('Std of salaries: ' + str(std10))
print ('Var of salaries: ' + str(var10))

# print block 2
print ('Sum of values, grouped by Formation: ' + str(groupby_sum1))
print ('Count of values, grouped by Formation: ' + str(groupby_count1))

print ('Sum of values, grouped by Noms: ' + str(groupby_sum2))
print ('Count of values, grouped by Noms: ' + str(groupby_count2))