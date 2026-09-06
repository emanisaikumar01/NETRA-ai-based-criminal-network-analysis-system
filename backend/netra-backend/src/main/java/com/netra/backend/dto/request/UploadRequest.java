package com.netra.backend.dto.request;

import jakarta.validation.constraints.NotBlank;

public record UploadRequest(

        @NotBlank(message = "Case ID is required")
        String caseId,

        String description

) {
}