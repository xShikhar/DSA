from collections import OrderedDict, defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0

        self.key_to_val = {}          # key -> value
        self.key_to_freq = {}         # key -> frequency
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> {key: None} in usage order

    def _bump_frequency(self, key: int) -> None:
        # move key from its current frequency bucket to the next one up
        freq = self.key_to_freq[key]
        del self.freq_to_keys[freq][key]

        # if that was the last key at min_freq, the min_freq bucket is now empty
        if freq == self.min_freq and len(self.freq_to_keys[freq]) == 0:
            self.min_freq += 1

        new_freq = freq + 1
        self.key_to_freq[key] = new_freq
        self.freq_to_keys[new_freq][key] = None  # append to "newest" end

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1

        self._bump_frequency(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._bump_frequency(key)
            return

        if len(self.key_to_val) >= self.capacity:
            # evict least frequently used, oldest among ties
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[evict_key]
            del self.key_to_freq[evict_key]

        # insert new key at frequency 1
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
