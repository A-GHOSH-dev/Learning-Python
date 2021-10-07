age=24
print("my age is "+str(age)+" years")
print("my age is {0} years.".format(age))
age='24'
print("my age is "+age+" years")
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31,"jan","mar","may","jul","aug","oct","dec"))
#replacement fields
print('''Jan:{2}
Feb:{0}
Mar:{2}
Apr:{1}
May:{2}
Jun:{1}'''.format(28,30,31))

#my age is 24 years
#my age is 24 years.
#my age is 24 years
#There are 31 days in jan, mar, may, jul, aug, oct and dec
#Jan:31
#Feb:28
#Mar:31
#Apr:30
#May:31
#Jun:30
      