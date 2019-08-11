class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return list(
            map(
                lambda x: "FizzBuzz" if x%3==0 and x%5==0 else "Fizz" if x%3==0 else "Buzz" if x%5==0 else str(x),list(range(1,n+1))
            )
        )
