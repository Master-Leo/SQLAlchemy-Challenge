# SQLAlchemy-Challenge
> I indulged in a series of climat analysis in the region of Hawaii

## Part 1: Analyze & Explore Climate Data 
- In this section, I utilized Python and SQLAlchemy to perform climate analys and data exploration through a database.
- I implemented SQLALchemy ORM queries, Pandas, and Matplotlib in the following steps: <br>
  1. Imported sqlite file and connected engine to SQLite database
  2. Automaped table classes to reference *station* and *measurements* later in the            process 
  3. Linked Python to the databse by creating a SQLAlchemy session 
  4. Performed a *percipitation* analysis then a *station* analysis
 <br>
 
 # Precipitation Analysis:
  1. Found recent date in the dataset
  2. Used recent date, retrieved prevoius 12 months of precipitation data by querying the     previous 12 months of data 
  3. Selected only the *DATE* and *PRCP* values
  4. Loaded the query into a Pandas DataFrame, and set the index to the 'date' column
  5. Sorted the DataFrame values by 'date'
  6. Plotted the results by using the DataFrame
  7. Utilized Pandas to print summary statistics for the precipitation data
  
 # Station Analysis:
  1. Designed a query to calculate the total number of stations in the dataset.
  2. Designed a query to find the most-active stations(most rows):
    - Listed the stations and observation counts in descending order
  3. Designed a query that calculated the lowest, highest, aqnd average temperatures          that filtered the most active station id found inthe previous query
  4. Designed aquery that retrieved prev 12 months of temperature observations data:
    - Filtered by the station that has the greatest number of observations
    - Queried the prev 12 months of TOBS data for that steation
    - Plotted the results as a histogram with bins=12
    
  ## Climate App
  > Created a Flask API based on the queries I just developed in the following steps:
  1. / 
    - Homepage
    - Listed all available routes <br>
  2. /api/v1.0/precipitation
    - 
  
  
