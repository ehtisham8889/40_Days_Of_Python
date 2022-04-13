# Importing necessary Libraries
import seaborn as sns
import matplotlib.pyplot as plt
# Importing Required Dataset
titanic=sns.load_dataset("titanic")
# bar plot Command
sns.barplot(x="fare", y="age",hue="class",data=titanic, color="red")
plt.title("Titanic Bar Plot")
plt.show()


