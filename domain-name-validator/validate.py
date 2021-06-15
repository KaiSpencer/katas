def validate(domain: str) -> bool:
    print("testssssssss", not is_top_level_domain_fully_numeric(domain))
    return all(
        [
            not is_longer_than_253_chars(domain),
            not more_than_127_levels(domain),
            valid_characters(domain),
            not all_levels_not_start_or_end_with_hyphen(domain),
            all_levels_not_longer_than_63_char(domain),
            not is_top_level_domain_fully_numeric(domain),
            is_enough_subdomains(domain),
        ]
    )


def is_longer_than_253_chars(domain):
    return len(domain) > 253


def more_than_127_levels(domain: str):
    return len(domain.split(".")) > 127


def valid_characters(domain: str):
    non_alphanum = [char for char in domain if not char.isalnum()]
    if non_alphanum:
        return all([char in "-." for char in non_alphanum])
    return True


def all_levels_not_start_or_end_with_hyphen(domain: str):
    levels = [level for level in domain.split(".")]
    return any(
        (level[0] == "-" if level else "") or (level[-1] == "-" if level else "")
        for level in levels
    )


def all_levels_not_longer_than_63_char(domain: str):
    return all([len(level) < 64 for level in domain.split(".")])


def is_top_level_domain_fully_numeric(domain: str):
    return domain.split(".")[-1].isnumeric()


def is_enough_subdomains(domain: str):
    return len(domain.split(".")) > 1
