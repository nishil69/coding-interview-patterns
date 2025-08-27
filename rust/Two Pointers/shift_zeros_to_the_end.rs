fn shift_zeros_to_the_end(nums: &mut Vec<i32>) {
    // The 'left' pointer is used to position non-zero elements.
    let mut left = 0;

    // Iterate through the array using a 'right' pointer to locate non-zero
    // elements.
    for right in 0..nums.len() {
        if nums[right] != 0 {
            nums.swap(left, right);
            // Increment 'left' since it now points to a position already occupied
            // by a non-zero element.
            left += 1;
        }
    }
}
