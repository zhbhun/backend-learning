// match
#[allow(dead_code)]
pub fn option_match(input: i32) -> bool {
    let x: Option<i32> = Some(input);
    match x {
        Some(_y) => true,
        None => false,
    }
}

// if
#[allow(dead_code)]
pub fn option_if(input: Option<i32>) -> i32 {
    if let Some(value) = input {
        value
    } else {
        0
    }
}

// ?
#[allow(dead_code)]
pub fn option_question(input: Option<i32>) -> Option<i32> {
    let value = input?;
    Some(value * 2)
}

// expect
#[allow(dead_code)]
pub fn option_expect(input: i32) -> i32 {
    let x: Option<i32> = Some(input);
    x.expect("This should not happen")
}

// unwrap
#[allow(dead_code)]
pub fn option_unwrap(input: i32) -> i32 {
    let x: Option<i32> = Some(input);
    x.unwrap()
}

// unwrap_or
#[allow(dead_code)]
pub fn option_unwrap_or(input: Option<i32>) -> i32 {
    input.unwrap_or(0)
}

// unwrap_or_else
#[allow(dead_code)]
pub fn option_unwrap_or_else(input: Option<i32>) -> i32 {
    input.unwrap_or_else(|| 0)
}

// map
#[allow(dead_code)]
pub fn option_map(input: Option<i32>) -> i32 {
    let result = input.map(|v| v * 2);
    result.unwrap_or(0)
}

// and_then
#[allow(dead_code)]
pub fn option_and_then(input: Option<i32>) -> i32 {
    let result = input.and_then(|v| Some(v * 2));
    result.unwrap_or(0)
}

// or
#[allow(dead_code)]
pub fn option_or(input: Option<i32>) -> i32 {
    let result = input.or(Some(0));
    result.unwrap()
}

// or_else
#[allow(dead_code)]
pub fn option_or_else(input: Option<i32>) -> i32 {
    let result = input.or_else(|| Some(0));
    result.unwrap()
}

// is_some
#[allow(dead_code)]
pub fn option_is_some(input: Option<i32>) -> i32 {
    if input.is_some() {
        input.unwrap()
    } else {
        0
    }
}

// is_none
#[allow(dead_code)]
pub fn option_is_none(input: Option<i32>) -> i32 {
    if input.is_none() {
        0
    } else {
        input.unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_option_match() {
        let result = option_match(1);
        assert_eq!(result, true);
    }

    #[test]
    fn test_option_if() {
        let result = option_if(None);
        assert_eq!(result == 0, true);
    }

    #[test]
    fn test_option_question() {
        assert_eq!(option_question(None).is_none(), true);
        assert_eq!(option_question(Some(1)).is_some(), true);
    }

    #[test]
    fn test_option_expect() {
        let result = option_expect(1);
        assert_eq!(result > 0, true);
    }

    #[test]
    fn test_option_unwrap() {
        let result = option_unwrap(1);
        assert_eq!(result > 0, true);
    }

    #[test]
    fn test_option_unwrap_or() {
        assert_eq!(option_unwrap_or(None) == 0, true);
        assert_eq!(option_unwrap_or(Some(1)) == 1, true);
    }

    #[test]
    fn test_option_unwrap_or_else() {
        assert_eq!(option_unwrap_or_else(None) == 0, true);
        assert_eq!(option_unwrap_or_else(Some(1)) == 1, true);
    }

    #[test]
    fn test_option_map() {
        assert_eq!(option_map(None) == 0, true);
        assert_eq!(option_map(Some(1)) == 2, true);
    }

    #[test]
    fn test_option_and_then() {
        assert_eq!(option_and_then(None) == 0, true);
        assert_eq!(option_and_then(Some(1)) == 2, true);
    }

    #[test]
    fn test_option_or() {
        assert_eq!(option_or(None) == 0, true);
        assert_eq!(option_or(Some(1)) == 1, true);
    }

    #[test]
    fn test_option_or_else() {
        assert_eq!(option_or_else(None) == 0, true);
        assert_eq!(option_or_else(Some(1)) == 1, true);
    }

    #[test]
    fn test_option_is_some() {
        assert_eq!(option_is_some(None) == 0, true);
        assert_eq!(option_is_some(Some(1)) == 1, true);
    }

    #[test]
    fn test_option_is_none() {
        assert_eq!(option_is_none(None) == 0, true);
        assert_eq!(option_is_none(Some(1)) == 1, true);
    }
}
