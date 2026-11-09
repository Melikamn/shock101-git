# Merge Conflict Report

## 1. Where did the conflict happen?

The conflict happened in `echo_lite.py`, in the line that defines the greeting response inside the `reply()` function.

Both branches modified the same line, but they used different greeting messages.

## 2. What did each branch contain?

The `main` branch had the casual greeting:

```python
return "Hey! What can I do for you?"
```

The `experiment/tone` branch had the formal greeting:

```python
return "Greetings. How may I assist you?"
```

Git could not automatically decide which version should be kept because both branches changed the same part of the file.

## 3. Understanding the conflict markers

Git displayed three important markers:

- `<<<<<<< HEAD` marked the version from the branch I was currently on (`main`).
- `=======` separated the two conflicting versions.
- `>>>>>>> experiment/tone` marked the version coming from the branch being merged.

These markers helped me identify exactly which changes were conflicting.

## 4. How I resolved the conflict

I reviewed both versions and decided to keep the casual greeting:

```python
return "Hey! What can I do for you?"
```

I chose this version because it gives Echo-lite a friendly and simple conversational personality.

I removed the conflict markers and the unwanted alternative, checked the resulting code, and completed the merge.

## 5. What I learned

I learned that a merge conflict is not necessarily a Git error. It happens when Git cannot automatically combine competing changes.

The important part is to understand both versions, make a deliberate decision, remove the conflict markers, and verify the final file before completing the merge.
