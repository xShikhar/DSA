class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq: dict[str, int] = {}
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])

            window_length = right - left + 1
            if window_length - max_freq > k:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1

            window_length = right - left + 1
            if window_length > max_length:
                max_length = window_length

        return max_length
