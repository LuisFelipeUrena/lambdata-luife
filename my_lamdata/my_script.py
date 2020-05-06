from my_lamdata.assign import cat_variables
from my_lamdata.assign import null_val
import pandas

data = {'a': [2, 5, 8, 9, 6, 2, 5, 5, 2],
        'b': [2, 5, 4, 7, 8, 2, 5, 4, 3]
        }

df = pandas.DataFrame(data)

null_val(df)

cat_variables(df)
