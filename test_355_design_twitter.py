import heapq


class Twitter:

    def __init__(self):
        # user_post = list[tuple[timestamp, tweet_id]]
        self.user_post: list[list[tuple[int, int]]] = [list() for _ in range(501)]
        # user_follow[user_id] = set of users followed by user_id
        self.user_follow: list[set[int]] = [{followed_user} for followed_user in range(501)]
        # timestamp counter
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Composes a new tweet with ID tweetId by the user userId.
        Each call to this function will be made with a unique tweetId"""
        self.user_post[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def follow(self, followerId: int, followeeId: int) -> None:
        """The user with ID followerId started following the user with ID followeeId."""
        self.user_follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """The user with ID followerId started unfollowing the user with ID followeeId."""
        self.user_follow[followerId].discard(followeeId)

    def getNewsFeed(self, userId: int) -> list[int]:
        """Retrieves the 10 most recent tweet IDs in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user himself.
        Tweets must be ordered from most recent to least recent."""
        NEWS_FEED_LENGTH = 10
        unfiltered_news_feed = []
        for followed_user in self.user_follow[userId]:
            posts_by_followed_user = self.user_post[followed_user]
            # get only last posts
            last_posts = posts_by_followed_user[-NEWS_FEED_LENGTH:]
            unfiltered_news_feed += last_posts
        # get largest 10 using heap
        return [tweet_id for _, tweet_id in heapq.nlargest(NEWS_FEED_LENGTH, unfiltered_news_feed)]


def test_edge_cases():
    twitter = Twitter()
    assert twitter.getNewsFeed(1) == []
    # 2 follows 1
    twitter.follow(2, 1)
    assert twitter.getNewsFeed(1) == []
    twitter.postTweet(1, 101)
    assert twitter.getNewsFeed(1) == [101]
    assert twitter.getNewsFeed(2) == [101]
    twitter.unfollow(2, 1)
    assert twitter.getNewsFeed(2) == []

    twitter = Twitter()
    twitter.follow(2, 1)
    twitter.follow(3, 1)
    twitter.postTweet(1, 101)
    assert twitter.getNewsFeed(1) == [101]
    assert twitter.getNewsFeed(2) == [101]
    assert twitter.getNewsFeed(3) == [101]
    twitter.postTweet(2, 102)
    assert twitter.getNewsFeed(1) == [101]
    assert twitter.getNewsFeed(2) == [102, 101]
    assert twitter.getNewsFeed(3) == [101]
    twitter.postTweet(1, 103)
    assert twitter.getNewsFeed(1) == [103, 101]
    assert twitter.getNewsFeed(2) == [103, 102, 101]
    assert twitter.getNewsFeed(3) == [103, 101]


def test_examples():
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]
