# lambdata-luife
Practice repo
## Installation
download this repo and make a copy of it
```sh
pipenv install
pipenv shell
```
## Usage
you can download this package with pip
```
pip install https://test.pypi.org/project/lambdata-luife/1.0/

```
## my_lamdata.assign.null_val
this functions shows the null values in any given pandas dataframe object
```py
from my_lamdata.assign import null_val
import pandas as pd
# dictionary to build our dataframe
data = {'a':[2,5,8,9,6,2,5,5,2],
'b':[2,5,4,7,8,2,5,4,3]
}
# instanciating the dataframe object in pandas 

df = pd.DataFrame(data)
#calling our function to check for nulls
null_val(df)

>>>Null Values in each Column
---------------------------
a    0
b    0
dtype: int64
---------------------------
```

## my_lamdata.assign.cat_variables
this function allows to describe the categorical variables in our dataframe pandas object

```py
from my_lamdata.assign import cat_variables
import pandas as pd 
#creating a dictionary variable
data = data = {'a':[2,5,8,9,6,2,5,5,2],
               'b':[2,5,4,7,8,2,5,4,3],
               'c':['good','bad','good','bad','good','bad','good','bad','bad']}
#instanciating the pandas dataframe object
df = pd.DataFrame(data) 

#calling out function
cat_variables(df)
```





