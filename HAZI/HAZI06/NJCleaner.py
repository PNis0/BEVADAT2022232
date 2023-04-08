import pandas as pd

class NJCleaner():
    def __init__(self, csvPath):
        self.data=pd.read_csv(csvPath)

    def order_by_scheduled_time(self):
        return self.data.sort_values('scheduled_time')
    
    def drop_columns_and_nan(self):
        self.data.drop(['from','to'], axis=1)
        self.drop.dropna()
        return self.data
    
    def convert_date_to_day(self):
        self.data['day']=pd.to_datetime(self.data['date']).dt.day_name()
        self.data=self.data.drop(['date'],axis=1)
        return self.data
    
    def convert_scheduled_time_to_part_of_the_day(self):
        def get_part_of_day(hour):
            if 4 <= hour < 8:
                return 'early_morning'
            elif 8 <= hour < 12:
                return 'morning'
            elif 12 <= hour < 16:
                return 'afternoon'
            elif 16 <= hour < 20:
                return 'evening'
            elif 20 <= hour <= 23:
                return 'night'
            else:
                return 'late_night'
        
        self.data['part_of_the_day'] = pd.to_datetime(self.data['scheduled_time']).dt.hour.apply(get_part_of_day)
        self.data = self.data.drop(['scheduled_time'], axis=1)
        return self.data
    
    def convert_delay(self):
        self.data['delay']=self.data['delay_minutes'].apply(lambda x:1 if x>=5 else 0)
        return self.data
    
    def drop_unnecessary_columns(self):
        self.data = self.data.drop(['train_id', 'scheduled_time', 'actual_time', 'delay_minutes'], axis=1)
        return self.data
    
    def save_first_60k(self,output_path):
        self.data.iloc[:60000].to_csv(output_path, index=False)

    def prep_df(self, file_path='data/NJ.csv'):
        df = self.order_by_scheduled_time()
        df = self.drop_columns_and_nan()
        df = self.convert_date_to_day()
        df = self.convert_scheduled_time_to_part_of_the_day()
        df = self.convert_delay()
        df = self.drop_unnecessary_columns()
        self.save_first_60k(file_path)
        return df


