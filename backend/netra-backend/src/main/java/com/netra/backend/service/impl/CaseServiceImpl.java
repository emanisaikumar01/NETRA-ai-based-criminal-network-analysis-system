package com.netra.backend.service.impl;

import com.netra.backend.dto.request.CaseCreateRequest;
import com.netra.backend.dto.request.CaseUpdateRequest;
import com.netra.backend.dto.response.CaseResponse;
import com.netra.backend.exception.ResourceNotFoundException;
import com.netra.backend.service.CaseService;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class CaseServiceImpl implements CaseService {

    /*
     * Temporary in-memory storage.
     *
     * This will be replaced with CaseRepository
     * after the PostgreSQL schema is finalized.
     */
    private final Map<String, CaseResponse> cases =
            new ConcurrentHashMap<>();

    @Override
    public CaseResponse createCase(CaseCreateRequest request) {

        String id = UUID.randomUUID().toString();

        CaseResponse caseResponse = new CaseResponse(
                id,
                request.title(),
                request.description(),
                "OPEN"
        );

        cases.put(id, caseResponse);

        return caseResponse;
    }

    @Override
    public CaseResponse getCaseById(String id) {

        CaseResponse caseResponse = cases.get(id);

        if (caseResponse == null) {
            throw new ResourceNotFoundException(
                    "Case not found with id: " + id
            );
        }

        return caseResponse;
    }

    @Override
    public List<CaseResponse> getAllCases() {

        return new ArrayList<>(cases.values());
    }

    @Override
    public CaseResponse updateCase(
            String id,
            CaseUpdateRequest request
    ) {

        CaseResponse existingCase = getCaseById(id);

        String title = request.title() != null
                ? request.title()
                : existingCase.title();

        String description = request.description() != null
                ? request.description()
                : existingCase.description();

        CaseResponse updatedCase = new CaseResponse(
                existingCase.id(),
                title,
                description,
                existingCase.status()
        );

        cases.put(id, updatedCase);

        return updatedCase;
    }

    @Override
    public void deleteCase(String id) {

        if (!cases.containsKey(id)) {
            throw new ResourceNotFoundException(
                    "Case not found with id: " + id
            );
        }

        cases.remove(id);
    }
}