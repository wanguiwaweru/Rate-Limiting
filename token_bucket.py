from time import time
from time import sleep


class TokenBucket():

    def __init__(self, bucket_size, refill_rate):
        """
        bucket_size: the maximum number of tokens allowed in the bucket
        refill_rate: number of tokens put into the bucket every second or other specified time period.
        """
        self.bucket_size = float(bucket_size)
        self._tokens = float(bucket_size)
        self.refill_rate = float(refill_rate)
        self.timestamp = time()

    def consume(self, tokens):
        """Consume tokens from the bucket. Returns True if there are tokens left else False."""
        if tokens <= self.tokens:
            self._tokens -= tokens
        else:
            return False
        return True

    def get_tokens(self):
        now = time()
        if self._tokens < self.bucket_size:
            delta = self.refill_rate * (now - self.timestamp)
            self._tokens = min(self.bucket_size, self._tokens + delta)
        self.timestamp = now
        return self._tokens

    tokens = property(get_tokens)


if __name__ == '__main__':

    # bucket with 80 tokens and refill rate of 1 token per seccond
    bucket = TokenBucket(80, 1)
    print("tokens =", bucket.tokens)
    print("consume(10) =", bucket.consume(10))
    print("consume(10) =", bucket.consume(10))
    sleep(1)
    print("tokens =", bucket.tokens)
    sleep(2)
    print("tokens =", bucket.tokens)
    print("consume(70) =", bucket.consume(70))
