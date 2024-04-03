use std::env;

#[allow(dead_code)]
pub fn temp_dir_path1() -> String {
    env::temp_dir().display().to_string()
}

#[allow(dead_code)]
pub fn temp_dir_path2() -> String {
    env::var("TMPDIR").unwrap_or_else(|_| "/tmp".to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_temp_dir_path1() {
        let result = temp_dir_path1();
        print!("temp_dir_path1: {}", result);
        assert_eq!(result.len() > 0, true);
    }

    #[test]
    fn test_temp_dir_path2() {
        let result = temp_dir_path1();
        print!("temp_dir_path2: {}", result);
        assert_eq!(result.len() > 0, true);
    }
}
