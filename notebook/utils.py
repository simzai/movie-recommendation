def weighted_ratings(df,m,c):
    v=df['vote_count']
    R=df['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * c)

