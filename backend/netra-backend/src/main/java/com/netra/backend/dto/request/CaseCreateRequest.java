package com.netra.backend.dto.request;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public record CaseCreateRequest(

        @NotBlank(message = "Case title is required")
        @Size(
                max = 200,
                message = "Case title must not exceed 200 characters"
        )
        String title,

        @Size(
                max = 2000,
                message = "Description must not exceed 2000 characters"
        )
        String description

) {
}