from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None

    result = []

    for idx, lst in enumerate(lst_of_lst, 1):
        result.extend(lst)
        if idx < len(lst_of_lst):
            result.append(sep)

    return result


if __name__ == "__main__":
    print("main")
    print(join_lists([["a,", "b"], ["c"]], "&"))
    print(join_lists([["a,", "b"], ["c"], ["d", "e"]], "&"))
