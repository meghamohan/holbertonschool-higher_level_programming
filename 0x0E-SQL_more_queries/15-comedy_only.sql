-- list all the comedy shows
SELECT tv_shows.title FROM tv_shows
    JOIN tv_show_genres
       	ON tv_shows.id=tv_show_genres.show_id
    WHERE tv_genres.name = 'Comedy'
    ORDER by tv_shows.title;
