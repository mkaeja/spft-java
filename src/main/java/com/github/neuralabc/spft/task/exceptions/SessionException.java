package com.github.neuralabc.spft.task.exceptions;

/**
 * An error running a session
 */
public class SessionException extends RuntimeException {
    public SessionException(String shortError, Exception exc) {
        super(shortError, exc);
    }
}