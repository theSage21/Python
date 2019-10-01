# NguyenU

def find_max(nums: List[int]) -> None:
    max = nums[0]
    for x in nums:
      if x > max:
        max = x
    print(max)

def main() -> None:
  find_max([2, 4, 9, 7, 19, 94, 5])

if __name__ == '__main__':
  main()
