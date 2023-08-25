import pandas

my_student = {
	"students": ["mekus", "daddy", "mysweet"],
	"scores": [76, 74, 90]

	}

data = pandas.DataFrame(my_student)
data.to_csv("new_data.csv")
