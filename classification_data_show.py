from sklearn.datasets import load_iris
iris = load_iris()
print iris.feature_names
print iris.target_names
for i in range(len(iris.target)):
	print "label %s and features %s" %(iris.target[i], iris.data[i]) 
