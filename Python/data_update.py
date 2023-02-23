import pandas
import numpy

def main():
    titles = ['Rank', 'Name', 'Platform', 'Year','Genre', 'Publisher',
                'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_sales', 'Global_Sales',
                'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Rating']

    db = numpy.array(pandas.read_csv('vgsales.csv')).tolist()
    for i in range(len(db)):
        db = [i+1] + db[i]
    # db = [[i+1] + db[i] for i in range(len(db))]

    df = dict()
    
    # for i in range (len(titles)):
    #     df[titles[i]] = [df[j][i] for j in range(len(db))]

    for i in range (len(titles)):
        for j in range(len(db)):
            df[titles[i]] = df[j][i]



    df = pandas.DataFrame(df, column=titles)
    df.to_csv('vgsales_new.csv', index= False)    

