from abc import ABC, abstractmethod


class Challenge(ABC):

    @abstractmethod
    def __init__(self, number, title):
        self.number = number
        self.title = title
        
    @abstractmethod
    def verify(self, val):
        pass

    @abstractmethod
    def pretty_title(self):
        pass


class BlogChallenge(Challenge):
    def __init__(self, number, title, merged_prs):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    @property
    def pretty_title(self):
        return f"PCC{self.number} - {self.title}"

    def verify(self, val):
        return val in self.merged_prs


class BiteChallenge(Challenge):
    def __init__(self, number, title, result):
        super().__init__(number, title)
        self.result = result

    @property
    def pretty_title(self):
        return f"Bite {self.number}. {self.title}"

    def verify(self, val):
        return val == self.result
    
        
if __name__ == '__main__':
    blog_challenge = BlogChallenge(24, "TestChallenge", [42, 7])
    print(blog_challenge.pretty_title)
    print(blog_challenge.verify(10))
    
    bite_challenge = BiteChallenge(24, "TestChallenge", "my result")
    print(bite_challenge.pretty_title)
    print(bite_challenge.verify("my result"))

    
