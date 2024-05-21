# Import necessary libraries
import concurrent.futures
import newspaper

# List of URLs to fetch headlines from
URLs = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.derspiegel.de/',
        'http://www.bbc.co.uk/',
        'https://theguardian.com']

# Function to fetch headlines from a given URL
def get_headlines(url):
    # Build the newspaper object for the given URL
    result = newspaper.build(url, memoize_articles=False)
    # Collect headlines in a list
    headlines = []
    for i in range(5):
        art = result.articles[i]
        art.download()
        art.parse()
        headlines.append(art.title)  # Append each headline to the list
    headlines.sort()  # Sort the list of headlines alphabetically
    # Print the sorted headlines
    print('\n''The headlines from %s are' % url, '\n')
    for headline in headlines:
        print(headline)

# Function to fetch headlines from all URLs concurrently
def get_headlines_concurrent():
    # Use ThreadPoolExecutor to fetch headlines concurrently with a maximum of 5 workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit tasks to fetch headlines for each URL
        future_to_url = {executor.submit(get_headlines, url): url for url in URLs}
        # As each task completes, print the result or handle exceptions
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))

# Main function
if __name__ == '__main__':
    # Measure the time taken to fetch headlines concurrently
    import timeit
    elapsed_time = timeit.timeit("get_headlines_concurrent()", setup="from __main__ import get_headlines_concurrent", number=1)
    print(elapsed_time)  # Print the elapsed time
