package com.netra.backend.service;

import com.netra.backend.dto.response.EvidenceResponse;

import java.util.List;

public interface EvidenceService {

    EvidenceResponse getEvidenceById(String id);

    List<EvidenceResponse> getEvidenceByCaseId(
            String caseId
    );
}