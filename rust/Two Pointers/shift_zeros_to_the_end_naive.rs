fn shift_zeros_to_the_end_naive(nums: &mut Vec<i32>) {
    let mut temp = vec![0; nums.len()];
    let mut i = 0;

    // Add all non-zero elements to the left of 'temp'.
    for num in nums.iter() {
        if *num != 0 {
            temp[i] = *num;
            i += 1;
        }
    }

    // Set 'nums' to 'temp'.
    for j in 0..nums.len() {
        nums[j] = temp[j];
    }
}
