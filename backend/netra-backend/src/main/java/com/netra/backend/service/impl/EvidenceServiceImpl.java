package com.netra.backend.service.impl;

import com.netra.backend.dto.response.EvidenceResponse;
import com.netra.backend.exception.ResourceNotFoundException;
import com.netra.backend.service.EvidenceService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EvidenceServiceImpl implements EvidenceService {

    @Override
    public EvidenceResponse getEvidenceById(String id) {

        /*
         * Temporary implementation.
         *
         * PostgreSQL integration will be added after
         * the database schema is finalized.
         */
        throw new ResourceNotFoundException(
                "Evidence not found with id: " + id
        );
    }

    @Override
    public List<EvidenceResponse> getEvidenceByCaseId(
            String caseId
    ) {

        /*
         * Temporary implementation.
         *
         * Evidence will be retrieved from PostgreSQL
         * after the database schema is finalized.
         */
        return List.of();
    }
}