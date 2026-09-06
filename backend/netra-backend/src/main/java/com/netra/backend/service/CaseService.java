package com.netra.backend.service;

import com.netra.backend.dto.request.CaseCreateRequest;
import com.netra.backend.dto.request.CaseUpdateRequest;
import com.netra.backend.dto.response.CaseResponse;

import java.util.List;

public interface CaseService {

    CaseResponse createCase(CaseCreateRequest request);

    CaseResponse getCaseById(String id);

    List<CaseResponse> getAllCases();

    CaseResponse updateCase(
            String id,
            CaseUpdateRequest request
    );

    void deleteCase(String id);
}