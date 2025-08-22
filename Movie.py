import json
from RedditStats import initialize_reddit_client, get_reddit_data
from OMDbStats import get_imdb_data
from TumblrStats import TumblrStats
from Mathplot import Mathplotlib

def main():
    # Movie list
    MOVIES_LIST = [
        "Disaster Movie", "Snow White", "Fifty Shades of Grey", "The Emoji Movie", "Slender Man", 
        "Max Steel", "The Dark Tower", "Man of Steel", "The 5th Wave", "21 Jump Street", 
        "The Great Wall", "Robin Hood", "Avengers: Infinity War", "Deadpool", "Cats", 
        "Logan", "Wonder Woman", "The Shape of Water", "The Matrix","Thuppakki"
    ]

    # Initialize API clients
    reddit_client = initialize_reddit_client()
    tumblr_client = TumblrStats(api_key="ygLC61xlnwf6j2XxXlDFDv2yk4ykjU2UJsRM92sRQr32Xyrfo9")

    # Collect data
    movie_stats = {}
    for movie in MOVIES_LIST:
        reddit_upvotes, reddit_comments = get_reddit_data(reddit_client, movie)
        imdb_rating, imdb_reviews = get_imdb_data(movie)
        tumblr_avg_notes = tumblr_client.get_tumblr_data(movie)
        
        movie_stats[movie] = {
            "reddit": {
                "upvotes": reddit_upvotes,
                "comments": reddit_comments
            },
            "imdb": {
                "rating": imdb_rating,
                "reviews": imdb_reviews
            },
            "tumblr": {
                "avg_notes": tumblr_avg_notes
            }
        }
        
        print(f"Movie: {movie}")
        print(f"   Reddit - Upvotes: {reddit_upvotes}, Comments: {reddit_comments}")
        print(f"   IMDb   - Rating: {imdb_rating}, Reviews: {imdb_reviews}")
        print(f"   Tumblr - Average Top 5 Notes: {tumblr_avg_notes:.2f}\n")
    
    # Write the dictionary to a text file in JSON format
    with open("movie_stats.txt", "w") as f:
        json.dump(movie_stats, f, indent=4)

    # Sort movies by IMDb Rating
    sorted_movies = sorted(
        movie_stats.keys(),
        key=lambda movie: float(movie_stats[movie]["imdb"]["rating"]) 
        if movie_stats[movie]["imdb"]["rating"] not in ("N/A", "", None) else 0.0
    )

    # User menu
    print("Select one comparison option:")
    print("1. IMDb Rating vs Reddit Upvotes")
    print("2. IMDb Rating vs Reddit Comments")
    print("3. IMDb Rating vs Tumblr Average Notes")
    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == "1":
        y_label = "Reddit Upvotes"
        y_func = lambda movie: movie_stats[movie]["reddit"]["upvotes"]
    elif choice == "2":
        y_label = "Reddit Comments"
        y_func = lambda movie: movie_stats[movie]["reddit"]["comments"]
    elif choice == "3":
        y_label = "Tumblr Average Notes"
        y_func = lambda movie: movie_stats[movie]["tumblr"]["avg_notes"]
    else:
        print("Invalid choice. Exiting.")
        return

    # Prepare data for plotting
    x_values = [
        float(movie_stats[movie]["imdb"]["rating"]) 
        if movie_stats[movie]["imdb"]["rating"] not in ("N/A", "", None) else 0.0 
        for movie in sorted_movies
    ]
    y_values = [y_func(movie) for movie in sorted_movies]

    # Plot the graph
    graph = Mathplotlib()
    graph.plot_graph(
        x_values, y_values, 
        x_label="IMDb Rating", 
        y_label=y_label, 
        sorted_movies=sorted_movies
    )

if __name__ == "__main__":
    main()
