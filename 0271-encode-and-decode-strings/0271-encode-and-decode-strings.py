class Codec:
    def encode(self, strs: List[str]) -> str:
        # print(len(strs))
        return "啊".join(strs)
            
    def decode(self, s: str) -> List[str]:
        return s.split("啊")
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))