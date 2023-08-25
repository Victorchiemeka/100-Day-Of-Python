import pandas as pd

data = pd.read_csv("nydata.csv")

the_color = data["Primary Fur Color"]
filtered_color = the_color[the_color == "Gray"]
bfilter = the_color[the_color == "Black"]
cfilter = the_color[the_color == "Cinnamon"]
gray_len = len(filtered_color)
b_len = len(bfilter)
c_len = len(cfilter)
print(gray_len)
print(c_len)
print(b_len)

my_data = {
	"fur_color": ["grey", "red", "black"],
	"count": [gray_len, c_len, b_len]
	
	}

create = pd.DataFrame(my_data)
create.to_csv("framedata.csv")
